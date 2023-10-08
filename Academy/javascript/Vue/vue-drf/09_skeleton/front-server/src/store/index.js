import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    articles: [
      
    ],
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    getArticles(context) {
      axios({
        mehtod: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
      .then((res) => {
        // console.log(res, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  modules: {
  }
})
