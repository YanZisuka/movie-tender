import drf from "@/api/drf";
import router from "@/router";
import axios from "axios";
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default {
  state: {
    token: localStorage.getItem("token") || "",
    currentUser: {},
    profile: {},
    authError: null,
    showAccountModal: false,
  },

  getters: {
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    profile: (state) => state.profile,
    authError: (state) => state.authError,
    authHeader: (state) => ({ Authorization: `Token ${state.token}` }),
    showAccountModal: (state) => state.showAccountModal,
  },

  mutations: {
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, profile) => (state.profile = profile),
    SET_AUTH_ERROR: (state, error) => (state.authError = error),
    SWITCH_SHOW_ACCOUNT_MODAL: (state) =>
      (state.showAccountModal = !state.showAccountModal),
  },

  actions: {
    saveToken({ commit }, token) {
      commit("SET_TOKEN", token);
      localStorage.setItem("token", token);
    },

    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("token", "");
    },

    login({ commit, dispatch }, credentials) {
      return axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          // router.push({ name: "index" });
          commit("SWITCH_SHOW_ACCOUNT_MODAL");
        })
        .catch((err) => {
          if (err.response.status === 400) {
            commit("SET_AUTH_ERROR", {
              non_field_errors: ["올바른 회원정보를 입력해주세요!"],
            });
            setTimeout(() => commit("SET_AUTH_ERROR", null), 4000);
          } else {
            commit("SET_AUTH_ERROR", err.response.data);
          }
          return err;
        });
    },

    signup({ commit, dispatch }, credentials) {
      return axios({
        url: drf.accounts.signup(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          // router.push({ name: "index" });
          commit("SWITCH_SHOW_ACCOUNT_MODAL");
        })
        .catch((err) => {
          console.error(err);
          if (err.response.status === 400) {
            commit("SET_AUTH_ERROR", {
              non_field_errors: [
                "비밀번호는 영문, 숫자를 포함한 8자 이상이어야 해요!",
              ],
            });
            setTimeout(() => commit("SET_AUTH_ERROR", null), 4000);
          } else {
            commit("SET_AUTH_ERROR", err.response.data);
          }
          return err;
        });
    },

    logout({ getters, dispatch, state }) {
      return axios({
        url: drf.accounts.logout(),
        method: "post",
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch("removeToken");
          state.currentUser = "";
          alert("다음에 또 놀러오세요!");
          router.push({ name: "index" });
        })
        .catch((err) => console.error(err.response));
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        return axios({
          url: drf.accounts.currentUserInfo(),
          method: "get",
          headers: getters.authHeader,
        })
          .then((res) => commit("SET_CURRENT_USER", res.data))
          .catch((err) => {
            if (err.response === 401) {
              dispatch("removeToken");
              router.push({ name: "index" });
            }
          });
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      return axios({
        url: drf.accounts.profile(username),
        method: "get",
        headers: getters.authHeader,
      }).then((res) => {
        commit("SET_PROFILE", res.data);
      });
    },

    updateUser({ commit, getters }, { username, nickname }) {
      return axios({
        url: drf.accounts.profile(username),
        method: "put",
        data: { nickname },
        headers: getters.authHeader,
      }).then((res) => {
        commit("SET_PROFILE", res.data);
      });
    },

    deleteUser({ commit, getters }, username) {
      if (confirm("탈퇴하시겠습니까?")) {
        return axios({
          url: drf.accounts.profile(username),
          method: "delete",
          headers: getters.authHeader,
        })
          .then(() => {
            commit("SET_PROFILE", {});
            router.push({ name: "index" });
          })
          .catch((err) => console.error(err.response));
      }
    },

    switchShowAccountModal({ commit }) {
      commit("SWITCH_SHOW_ACCOUNT_MODAL");
    },
  },
};
