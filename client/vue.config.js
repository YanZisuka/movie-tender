const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      scss: {
        additionalData: `
          @import "@/styles/_variable.scss";
          @import "@/styles/reset.scss";
          @import "@/styles/index.scss";
          @import "@/styles/button.scss";
          @import "@/styles/text.scss";
          @import "@/styles/scrollbar.scss";
        `,
      },
    },
  },
});
