import { writable } from "svelte/store";

export const storeThemes = writable("dark");

/**
 * It exports a writable store called storeThemes.
 * This store is used to manage the theme of the application.
 * It has two methods: toggleThemeLight and toggleThemeDark.
 * The storeThemes store is exported so that it can be used in other parts of the application to subscribe to changes in the theme and update the theme.
 */
export default {
  subscribe: storeThemes.subscribe,
  toggleThemeLight: () => storeThemes.update((themeColor) => "light"),
  toggleThemeDark: () => storeThemes.update((themeColor) => "dark"),
};
