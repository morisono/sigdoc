# ZenHub Rednine

- [Zenhub - Agile Project Management for Software Teams](https://www.zenhub.com/)
- [ZenHub for GitHub - Chrome ウェブストア](https://chromewebstore.google.com/detail/zenhub-for-github/ogcgkffhplmphkaahpmffcafajaocjbd?hl=ja)


GitHub Issues、Label、Milestone、Projects と組み合わせて運用

### GitHub Projects
```bash
gh project --help
Work with GitHub Projects. Note that the token you are using must have 'project' scope, which is not set by default. You can verify your token scope by running 'gh auth status' and add the project scope by running 'gh auth refresh -s project'.

USAGE
  gh project <command> [flags]

AVAILABLE COMMANDS
  close:       Close a project
  copy:        Copy a project
  create:      Create a project
  delete:      Delete a project
  edit:        Edit a project
  field-create: Create a field in a project
  field-delete: Delete a field in a project
  field-list:  List the fields in a project
  item-add:    Add a pull request or an issue to a project
  item-archive: Archive an item in a project
  item-create: Create a draft issue item in a project
  item-delete: Delete an item from a project by ID
  item-edit:   Edit an item in a project
  item-list:   List the items in a project
  link:        Link a project to a repository or a team
  list:        List the projects for an owner
  mark-template: Mark a project as a template
  unlink:      Unlink a project from a repository or a team
  view:        View a project

INHERITED FLAGS
  --help   Show help for command

EXAMPLES
  $ gh project create --owner monalisa --title "Roadmap"
  $ gh project view 1 --owner cli --web
  $ gh project field-list 1 --owner cli
  $ gh project item-list 1 --owner cli

LEARN MORE
  Use `gh <command> <subcommand> --help` for more information about a command.
  Read the manual at https://cli.github.com/manual
```

```bash
gh project item-create 4 --owner That-Lady-Dev --title "Test Adding Draft" --body "I added this draft issue with GitHub CLI"
```

```bash
gh project copy 1 --source-owner That-Lady-Dev --target-owner Demos-and-Donuts --title "copied project"
```

```bash
gh project item-add 4 --owner That-Lady-Dev --url https://github.com/Demos-and-Donuts/video-to-gif-converter/issues/1
```


- [Best practices for Projects - GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects)
- [10 things you didn’t know you could do with GitHub Projects - The GitHub Blog](https://github.blog/developer-skills/github/10-things-you-didnt-know-you-could-do-with-github-projects/#2-export-your-projects-to-tsv)

### Exporter

- [GitHub - fiedl/github-project-to-csv: Simple cli to export github v2 projects to csv](https://github.com/fiedl/github-project-to-csv)
- [GitHub - justinmahar/github-projectv2-csv-exporter: 📂 Export GitHub project cards as CSV files. Uses the ProjectV2 API.](https://github.com/justinmahar/github-projectv2-csv-exporter)
- [Tools / GitHub Project Exporter - Exporter ⋅ Storybook](https://justinmahar.github.io/github-projectv2-csv-exporter/?path=/story/tools-github-project-exporter--exporter)
- [Using the API to manage Projects - GitHub Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects)


## Redmine

- redmine-evolution
- easy-redmine
- hosting-redmine
- Lychee redmine

- [Openproject](https://www.openproject.org/)

-[「Redmine 8年分の新機能ふりかえり」Redmine 3.4 〜 Redmine 5.1から意外と知らない機能をピックアップ （入門Redmine 第6版 出版記念企画） - YouTube](https://www.youtube.com/watch?v=PXz8DzU1gDM)
- [GitHub Projects の始め方 〜社内のタスク管理にどうですか？〜 #GitHubProjects - Qiita](https://qiita.com/gotanda_kazutaka/items/ee2d330f1bd5fc9694e3)