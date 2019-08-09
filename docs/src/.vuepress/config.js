module.exports = {
  title: 'Wall',
  description: 'The Wall Programming Language',
  head: [
    ['link', { rel: 'icon', href: '/logo.png' }]
  ],
  themeConfig: {
    sidebar: [
      '/',
      {
        title: 'First steps',
        collapsable: true,
        children: [
          ['/getting', 'Getting Wall'],
          ['/anatomy', 'Anatomy'],
          ['/comments', 'Comments'],
          ['/symbols', 'Symbols'],
          ['/sets-1', 'Sets I'],
          ['/assignment', 'Assignment'],
          ['/lists', 'Lists'],
          ['/functions-1', 'Functions I'],
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
          ['/tests', 'Tests'],
          ['/sugar-1', 'Sugar I'],
        ]
      },
      {
        title: 'Exploring',
        collapsable: true,
        children: [
          ['/errors', 'Errors'],
          ['/functions-3', 'Functions III'],
          ['/sets-2', 'Sets II'],
          ['/sugar-2', 'Sugar II'],
          ['/validation-1', 'Validation I'],
          ['/functions-4', 'Functions IV'],
          ['/recursion', 'Recursion'],
          ['/validation-2', 'Validation II']
        ]
      },
      {
        title: 'Soaring',
        collapsable: true,
        children: [
          ['/modules', 'Modules'],
          ['/packages', 'Packages'],
          ['/indeterminacy', 'Indeterminacy'],
          ['/validation-3', 'Validation III'],
          ['/io', 'IO'],
          ['/threading', 'Threading'],
          ['/example', 'Example']
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
    ],
    // Assumes GitHub. Can also be a full GitLab url.
    repo: 'mikesol/wall',
    // Customising the header label
    // Defaults to "GitHub"/"GitLab"/"Bitbucket" depending on `themeConfig.repo`
    repoLabel: 'GitHub',

    // Optional options for generating "Edit this page" link

    // if your docs are in a different repo from your main project:
    docsRepo: 'mikesol/wall',
    // if your docs are not at the root of the repo:
    docsDir: 'docs/src',
    // if your docs are in a specific branch (defaults to 'master'):
    docsBranch: 'master',
    // defaults to false, set to true to enable
    editLinks: true,
    // custom text for edit link. Defaults to "Edit this page"
    editLinkText: 'Edit this page'
  }
}