import { Injectable } from '@angular/core';
import {
    HttpEvent,
    HttpInterceptor,
    HttpHandler,
    HttpRequest
} from '@angular/common/http';

import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';


@Injectable()
export class XsrfService {

  constructor(private cookie: CookieService) { }

    intercept (r: HttpRequest<any>, n: HttpHandler) : Observable <HttpEvent <any>> {
    return n.handle(r.clone({
      headers: r.headers.set('X-CSRFToken', this.cookie.get('csrftoken'))
    }));
  }

}