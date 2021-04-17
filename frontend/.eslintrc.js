// eslint rules to enforce code syntax, style is covered by prettier
module.exports = {
  env: {
    browser: true,
    node: true,
    es2021: true
  },
  extends: [
      "eslint:recommended",
      "plugin:react/recommended",
      // "prettier" // put last to override other configs
  ],
  ignorePatterns: [".idea/*", "assets/*", "build/*", "node_modules/*", "public/*"],
  parser: "babel-eslint",
  parserOptions: {
    babelOptions: {
      configFile: "./babel.config.json"
    },
    ecmaFeatures: {
      jsx: true
    },
    ecmaVersion: 12,
    sourceType: "module"
  },
  plugins: ["react"],
  rules: {
    "default-case": "error",
    "default-case-last": "warn",
    "no-empty-function": "warn",
    "no-unused-vars": ["error", {args: "none"}],
    "no-use-before-define": ["error", {classes: true, functions: false, variables: true}],
    "react/prop-types": "off",
    "react/no-unescaped-entities": "warn",
  },
  settings: {
    react: {
      version: "detect"
    },
    linkComponents: [
        // Components used as alternatives for <a> tags for linking, e.g., <Link to={URL} />
      {name: "Link", linkAttribute: "to"}
    ],
  },
};
