import { Store } from "vuex";
import type {
  RootState,
  AccountsState,
  CommunityState,
  MoviesState,
} from "@/types";

declare module "@vue/runtime-core" {
  type State = {} & RootState & AccountsState & CommunityState & MoviesState;

  interface ComponentCustomProperties {
    $store: Store<State>;
  }
}
