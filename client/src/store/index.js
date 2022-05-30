import Vue from 'vue'
import Vuex from 'vuex'
import createdPersistedState from 'vuex-persistedstate'

import accounts from './modules/accounts'
import movies from './modules/movies'
import community from './modules/community'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    accounts,
    movies,
    community,
  },

  plugins: [
    createdPersistedState({
      paths: ['accounts',],
    }),
  ],
})
