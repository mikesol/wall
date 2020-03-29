module.exports = {
  title: 'Wall',
  description: 'The Wall Programming Language',
  head: [
    ['link', { rel: 'icon', href: '/logo.png' }]
  ],
  themeConfig: {
    logo: '/logo.png',
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
          ['/assignment', 'Assignment'],
          ['/functions-1', 'Functions I'],
          ['/sets-1', 'Sets I'],
          ['/lists', 'Lists'],
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
          ['/tests-1', 'Tests I'],
          ['/syntax-1', 'Syntax I'],
        ]
      },
      {
        title: 'Exploring',
        collapsable: true,
        children: [
          ['/errors', 'Errors'],
          ['/functions-3', 'Functions III'],
          ['/sets-2', 'Sets II'],
          ['/syntax-2', 'Syntax II'],
          ['/functions-4', 'Functions IV'],
          ['/recursion', 'Recursion']
        ]
      },
      {
        title: 'Soaring',
        collapsable: true,
        children: [
          ['/modules', 'Modules'],
          ['/packages', 'Packages'],
          ['/indeterminacy', 'Indeterminacy'],
          ['/io', 'IO'],
          ['/tests-2', 'Tests 2'],
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