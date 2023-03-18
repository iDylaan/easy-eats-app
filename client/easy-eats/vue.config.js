const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    host: '0.0.0.0',
    port: 8080
  },
  transpileDependencies: true,
  css: {
    loaderOptions: {
      sass: {
        additionalData: `@import "@/assets/styles/main.scss";`
      }
    }
  }
})