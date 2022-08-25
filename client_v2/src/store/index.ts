import { createStore, StoreOptions } from "vuex";

import accounts from "@/store/modules/accounts";
import movies from "@/store/modules/movies";
import community from "@/store/modules/community";

import { RootState } from "@/types";

const store = createStore({
  modules: {
    accounts,
    movies,
    community,
  },
});

export default store;
