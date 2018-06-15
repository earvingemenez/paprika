import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TokenService } from './token.service';
import { XsrfService } from './xsrf.service';


@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [],
  providers: [TokenService, XsrfService]
})
export class InterceptorsModule { }
