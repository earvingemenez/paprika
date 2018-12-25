import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { UIRouterModule } from '@uirouter/angular';
import { CookieService } from 'ngx-cookie-service';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { PartialsModule } from './components/partials/partials.module';
import { PublicModule } from './components/public/public.module';
import { UsersModule } from './components/users/users.module';
import { BooksModule } from './components/books/books.module';

import { TokenService } from './commons/services/interceptors/token.service';
import { APP_STATES } from './commons/utils/app.states';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    UIRouterModule.forRoot(APP_STATES),
    NgbModule.forRoot(),

    PartialsModule,
    PublicModule,
    UsersModule,
    BooksModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: TokenService, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }