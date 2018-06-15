import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { UIRouterModule } from '@uirouter/angular';
import { CookieService } from 'ngx-cookie-service';

import { PublicModule } from './components/public/public.module';
import { UsersModule } from './components/users/users.module';
import { ServicesModule } from './commons/services/services.module';

import { XsrfService } from './commons/services/interceptors/xsrf.service';
import { TokenService } from './commons/services/interceptors/token.service';

import { APP_STATES } from './commons/states/app.states';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    UIRouterModule.forRoot(APP_STATES),
    
    ServicesModule,
    PublicModule,
    UsersModule
  ],
  providers: [
    CookieService,
    { provide: HTTP_INTERCEPTORS, useClass: XsrfService, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: TokenService, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
