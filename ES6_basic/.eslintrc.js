module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: ["airbnb-base", "plugin:jest/all"],
  globals: {
    Atomics: "readonly",
    SharedArrayBuffer: "readonly",
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: "module",
  },
  plugins: ["jest"],
  rules: {
    "no-console": "off",
    "no-shadow": "off",
    "no-restricted-syntax": ["error", "LabeledStatement", "WithStatement"],
    "indent": ["error", 2],  // Ajout de la règle d'indentation
    "no-trailing-spaces": "error",  // Ajout de la règle pour les trailing spaces
  },
  overrides: [
    {
      files: ["*.js"],
      excludedFiles: "babel.config.js",
    },
  ],
};
