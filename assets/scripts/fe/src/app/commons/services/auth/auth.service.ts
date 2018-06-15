import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { AUTH_LOGIN } from '../../constants/api.constants';
import { AUTH_KEY } from '../../constants/conf.constants';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http : HttpClient
  ) { }

  /* LOGIN USER.
   * @desc : send a request to the backend for the
   *         user generated token.
   */
  login (creds) {
    return this.http.post(AUTH_LOGIN, creds)
      .toPromise()
      .then(resp => {
        this.setToken(resp);

        return resp;
      })
      .catch(err => { return Promise.reject(err); })
    ;
  }


  /* GET / SET USER TOKEN
   * @desc : get and set user token to localStorage
   */
  setToken (d) {
    (<any>window).localStorage[AUTH_KEY] = JSON.stringify(d);
    return d;
  }

  getToken () {
    let d = (<any>window).localStorage[AUTH_KEY];
    if (!d) { return null; };

    return JSON.parse(d);
  }

  rmToken () {
    (<any>window).localStorage.removeItem(AUTH_KEY);
  }


  /* VALIDATORS
   * @desc : validates the auth user information
   */
  authenticated () {
    return this.getToken() ? true : false;
  }
}
