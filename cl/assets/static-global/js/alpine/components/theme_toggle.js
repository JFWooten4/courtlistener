/*
Color-mode state shared across new-design theme toggles. The initial value is
set synchronously in new_base.html before Tailwind is loaded, preventing a flash.
The storage key is retained from the legacy dark-mode proposal.
*/
const COLOR_MODE_KEY = 'cl-color-mode';

function readColorModePreference() {
  try {
    const mode = window.localStorage.getItem(COLOR_MODE_KEY);
    return mode === 'light' || mode === 'dark' ? mode : null;
  } catch (error) {
    return null;
  }
}

function systemColorMode(query) {
  return query && query.matches ? 'dark' : 'light';
}

document.addEventListener('alpine:init', () => {
  const mediaQuery = window.matchMedia
    ? window.matchMedia('(prefers-color-scheme: dark)')
    : null;

  Alpine.store('colorMode', {
    isDark: document.documentElement.dataset.colorMode === 'dark',

    setMode(mode, persist = false) {
      this.isDark = mode === 'dark';
      document.documentElement.dataset.colorMode = this.isDark ? 'dark' : 'light';
      if (persist) {
        try {
          window.localStorage.setItem(COLOR_MODE_KEY, mode);
        } catch (error) {
          // Browsing environments may restrict persistent storage.
        }
      }
    },

    toggle() {
      this.setMode(this.isDark ? 'light' : 'dark', true);
    },
  });

  Alpine.data('themeToggle', () => ({
    get isDark() {
      return Alpine.store('colorMode').isDark;
    },
    get label() {
      return this.isDark ? 'Use light mode' : 'Use dark mode';
    },
    get symbol() {
      return this.isDark ? '☀' : '☾';
    },
    toggle() {
      Alpine.store('colorMode').toggle();
    },
  }));

  window.addEventListener('storage', (event) => {
    if (event.key !== COLOR_MODE_KEY && event.key !== null) return;
    const mode = readColorModePreference() || systemColorMode(mediaQuery);
    Alpine.store('colorMode').setMode(mode);
  });

  if (mediaQuery) {
    const onSystemChange = (event) => {
      if (!readColorModePreference()) {
        Alpine.store('colorMode').setMode(systemColorMode(event));
      }
    };
    if (typeof mediaQuery.addEventListener === 'function') {
      mediaQuery.addEventListener('change', onSystemChange);
    } else if (typeof mediaQuery.addListener === 'function') {
      mediaQuery.addListener(onSystemChange);
    }
  }
});
