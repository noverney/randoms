// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: false,
  modules: [
    'nuxt-vuefire',
    '@nuxt/ui'
  ],
  vuefire: {
    auth: {
      enabled: true
    },
    config: {
      apiKey: 'AIzaSyAIyFQl-uumudGBDylUd40h83jSlAAztiE',
      authDomain: 'baselhack2023-randoms.firebaseapp.com',
      projectId: 'baselhack2023-randoms',
      appId: '1:1073309728716:web:e6c46bdb8d36fbedafa769',
    },
  },
})
