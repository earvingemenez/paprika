import { PUBLIC_STATES } from '../../components/public/public.states';
import { USERS_STATES } from '../../components/users/users.states';

export const APP_STATES = {
  otherwise: '/',
  states: [].concat(
    PUBLIC_STATES,
    USERS_STATES
  )
}