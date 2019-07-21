# Project Breakdown

assets — Where you put any assets that are imported into your components
components — All the components of the projects that are not the main views
mixins — The mixins are the parts of javascript code that is reused in different components. In a mixin you can put any component’s methods from Vue.js they will be merged with the ones of the component that uses it.
router — All the routes of your projects (in my case I have them in the index.js). Basically in Vue.js everything is a component. But not everything is a page. A page has a route like “/dashboard”, “/settings” or “/search”. If a component has a route it is routed.
store (optional) — The Vuex constants in mutation-type.js, the Vuex modules in the subfolder modules (which are then loaded in the index.js).
translations (optional) — Locales files, I use Vue-i18n, and it works pretty good.
utils (optional) — Functions that I use in some components, such as regex value testing, constants or filters.
views — To make the project faster to read I separate the components that are routed and put them in this folder. The components that are routed for me are more than a component since they represent pages and they have routes, I put them in “views” then when you check a page you go to this folder.


copied from https://itnext.io/how-to-structure-a-vue-js-project-29e4ddc1aeeb