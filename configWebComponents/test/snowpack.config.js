// Snowpack Configuration File
// See all supported options: https://www.snowpack.dev/reference/configuration

/** @type {import("snowpack").SnowpackUserConfig } */
module.exports = {
  mount: {
    /* ... */
  },
  plugins: [
    /* ... */
  ],
  packageOptions: {
    /* ... */
  },
  devOptions: {
    /* ... */
  },
  buildOptions: {
    /* ... */
  },
  packageOptions: {
    knownEntrypoints:["@polymer/paper-styles/color.js", "@polymer/polymer/lib/utils/settings.js","@polymer/polymer/lib/legacy/polymer.dom.js"]

  }
};
