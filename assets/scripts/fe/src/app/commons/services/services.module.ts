import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthService } from './auth/auth.service';
import { InterceptorsModule } from './interceptors/interceptors.module';


@NgModule({
  imports: [
    CommonModule,
    InterceptorsModule
  ],
  declarations: [],
  providers: [AuthService]
})
export class ServicesModule { }
