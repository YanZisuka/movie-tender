import { Module } from "vuex";

import axios from "axios";
import drf from "@/api/drf";
import router from "@/router";

import { AccountsState, RootState, User } from "@/types";

const accounts: Module<AccountsState, RootState> = {
  // namespaced: true,

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
    authHeader: (state) => ({
      Authorization: `Token ${state.token}`,
    }),
    showAccountModal: (state) => state.showAccountModal,
  },

  mutations: {
    SET_TOKEN: (state, token: string) => (state.token = token),
    SET_CURRENT_USER: (state, user: User) => (state.currentUser = user),
    SET_PROFILE: (state, profile: User) => (state.profile = profile),
    SET_AUTH_ERROR: (state, error: string) => (state.authError = error),
    SWITCH_SHOW_ACCOUNT_MODAL: (state) =>
      (state.showAccountModal = !state.showAccountModal),
  },

  actions: {
    saveToken({ commit }, token: string) {
      commit("SET_TOKEN", token);
      localStorage.setItem("token", token);
    },

    removeToken({ commit }) {
      commit("SET_TOKEN", "");
      localStorage.setItem("token", "");
    },

    login({ commit, dispatch }, credentials: Object) {
      axios({
        url: drf.accounts.login(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          router.push({ name: "index" });
        })
        .catch((err) => {
          console.error(err);
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },

    signup({ commit, dispatch }, credentials: Object) {
      axios({
        url: drf.accounts.signup(),
        method: "post",
        data: credentials,
      })
        .then((res) => {
          const token = res.data.key;
          dispatch("saveToken", token);
          dispatch("fetchCurrentUser");
          router.push({ name: "index" });
        })
        .catch((err) => {
          console.error(err);
          commit("SET_AUTH_ERROR", err.response.data);
        });
    },

    logout({ getters, dispatch, state }) {
      axios({
        url: drf.accounts.logout(),
        method: "post",
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch("removeToken");
          state.currentUser = "";
          alert("로그아웃 되었습니다.");
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
      axios({
        url: drf.accounts.profile(username),
        method: "put",
        data: { nickname },
        headers: getters.authHeader,
      }).then((res) => {
        commit("SET_PROFILE", res.data);
      });
    },

    deleteUser({ commit, getters }, username: string) {
      if (confirm("탈퇴하시겠습니까?")) {
        axios({
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

export default accounts;
