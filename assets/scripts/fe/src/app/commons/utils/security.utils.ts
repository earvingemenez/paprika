import { AuthService } from '../services/auth/auth.service';


export function LoginRequired (t) {
  let auth = t.injector().get(AuthService),
      state = t.router.stateService;

  if (!auth.authenticated()) return state.target('signin');
}

export function Disconnect (t) {
  let auth = t.injector().get(AuthService),
      state = t.router.stateService;

  if(auth.authenticated()) auth.rmToken();
  return state.target('signin');
}