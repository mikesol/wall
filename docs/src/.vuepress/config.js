module.exports = {
    title: 'Wall',
    description: 'The Wall Programming Language',
    themeConfig: {
        sidebar: [
          '/',
          {
            title: 'First steps',
            collapsable: true,
            children: [
              ['/anatomy', 'Anatomy'],
              ['/symbols', 'Symbols'],
              ['/sets-1', 'Sets I'],
              ['/assignment', 'Assignment'],
              ['/comments', 'Comments'],
              ['/pairs', 'Pairs'],
              ['/functions-1', 'Functions I'],
            ]
          },
          {
            title: 'Getting comfortable',
            collapsable: true,
            children: [
              ['/primitives', 'Primitive Types'],
              ['/numbers', 'Numbers'],
              ['/strings', 'Strings'],
              ['/booleans', 'Booleans'],
              ['/functions-2', 'Functions II'],
              ['/lists', 'Lists'],
              ['/functions-3', 'Functions III'],
              ['/recursion-1', 'Recursion I'],
              ['/sugar-1', 'Sugar I'],
            ]
          },
          {
            title: 'Exploring',
            collapsable: true,
            children: [
              ['/errors', 'Errors'],
              ['/functions-4', 'Functions IV'],
              ['/sets-2', 'Sets II'],
              ['/recursion-2', 'Recursion II'],
              ['/validation-1', 'Validation I'],
              ['/sugar-2', 'Sugar II'],
              ['/functions-5', 'Functions V'],
              ['/validation-2', 'Validation II']
            ]
          },
          {
            title: 'Soaring',
            collapsable: true,
            children: [
              ['/modules', 'Modules'],
              ['/packages', 'Packages'],
              ['/monads', 'Monads'],
              ['/bang', 'Bang'],
              ['/indeterminacy', 'Indeterminacy'],
              ['/io', 'IO'],
              ['/threading', 'Threading']
            ]
          },
          {
            title: 'Digging',
            collapsable: true,
            children: [
              ['/reference', 'Reference'],
              ['/proofs', 'Proofs'],
              ['/contributing', 'Contributing']
            ]
          },
        ]
      }
}