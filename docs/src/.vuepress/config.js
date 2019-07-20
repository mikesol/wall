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
              ['/comments', 'Comments'],
              ['/pairs', 'Pairs'],
              ['/functions-1', 'Functions I'],
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
              ['/lists-1', 'Lists I'],
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
              ['/functions-6', 'Functions VI'],
              ['/modules', 'Modules'],
              ['/packages', 'Packages'],
              ['/lists-2', 'Lists II'],
              ['/functions-7', 'Functions VII'],
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