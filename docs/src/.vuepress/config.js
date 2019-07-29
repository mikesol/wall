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
              ['/getting', 'Getting Wall'],
              ['/anatomy', 'Anatomy'],
              ['/symbols', 'Symbols'],
              ['/sets-1', 'Sets I'],
              ['/assignment', 'Assignment'],
              ['/lists', 'Lists'],
              ['/functions-1', 'Functions I'],
              ['/comments', 'Comments'],
              ['/tests', 'Tests'],
            ]
          },
          {
            title: 'Getting comfortable',
            collapsable: true,
            children: [
              ['/numbers', 'Numbers'],
              ['/strings', 'Strings'],
              ['/booleans', 'Booleans'],
              ['/functions-2', 'Functions II'],
              ['/functions-3', 'Functions III'],
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
              ['/sugar-2', 'Sugar II'],
              ['/validation-1', 'Validation I'],
              ['/functions-5', 'Functions V'],
              ['/recursion', 'Recursion'],
              ['/validation-2', 'Validation II']
            ]
          },
          {
            title: 'Soaring',
            collapsable: true,
            children: [
              ['/functions-6', 'Functions VI'],
              ['/modules', 'Modules'],
              ['/packages', 'Packages'],
              ['/indeterminacy', 'Indeterminacy'],
              ['/validation-3', 'Validation III'],
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
              ['/contributing', 'Contributing'],
              ['/musings', 'Musings']
            ]
          },
        ]
      }
}