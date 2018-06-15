import { AuthService } from '../services/auth/auth.service';


export function LoginRequired (t) {
  let auth = t.injector().get(AuthService);
  let state = t.router.stateService;

  if (!auth.authenticated()) { return state.target('login') }
}