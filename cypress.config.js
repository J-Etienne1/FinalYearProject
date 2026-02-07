const { defineConfig } = require("cypress");

module.exports = defineConfig({
  allowCypressEnv: false,

  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    this.baseUrl = 'http://127.0.0.1:8000/'
    },
  },
});
