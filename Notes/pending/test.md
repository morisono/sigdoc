```dataviewjs
// Don't change this code

const {createButton} = app.plugins.plugins["buttons"]
const tp = app.plugins.plugins["templater-obsidian"].templater.current_functions_object

let current = dv.current()
let currentFile = app.vault.getAbstractFileByPath(current.file.path)

const changeFilter = async(prop) => {
  let propName = "filter-" + prop
  let values = pages.map(p => p[prop])
  values = [...new Set(values)]
  values.unshift("all")
  let val = await tp.system.suggester(values, values)
    app.fileManager.processFrontMatter(currentFile, (frontmatter) => { 
		frontmatter[propName] = val
	})
  }

const filterButton = async(name, prop) => {
  createButton({
	app, 
	el: this.container, 
	args: {
		name: name}, 
	clickOverride: {
		click: await changeFilter, 
		params: [prop]
	}
  })
}

const filterFunction = async(prop) => {
  let propName = "filter-" + prop
  let filter = current[propName]
  if (filter != "all" && filter != null) {
	filteredPages = filteredPages.filter(p => p[prop] == filter)
  }
}




// Only edit the code below

let pages = dv.pages('"Test folder"')
let filteredPages = [...pages]


// Apply filters
await filterFunction("color")
await filterFunction("number")

// Add filter buttons
await filterButton("Filter color", "color")
await filterButton("Filter number", "number")


let headers = ["Name", "Color", "Number"]
let rows = filteredPages.map(p => [p.file.link, p.color, p.number])

dv.table(headers, rows)
```
tetests