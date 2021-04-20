// see documentation at https://prettier.io/docs/en/options.html
module.exports = {
    printWidth: 120,
    tabWidth: 4,
    useTabs: false,
    // add semicolon after each statement
    semi: true,
    // do not enforce single quote strings, default double, choose the one for least escaping
    singleQuote: false,
    quoteProps: "as-needed",
    // do not enforce single quotes in jsx(jsx is based on HTML double quotes)
    jsxSingleQuote: false,
    trailingComma: "es5",
    bracketSpacing: false,
    // do not reformat the jsx HTML to put ">" on the same line, m<ay lower visibility
    jsxBracketSameLine: false,
    // always put parentheses around inputs to arrow functions
    arrowParens: "always",
    // do not add or require indicator for prettier-usage
    requirePragma: false,
    insertPragma: false,
    // wrap markdown as-is
    proseWrap: "preserve",
    htmlWhitespaceSensitivity: "css",
    endOfLine: "lf",
    // do not try to format "recognized" code in strings
    embeddedLanguageFormatting: "off"
}
