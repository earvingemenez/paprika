import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UIRouterModule } from '@uirouter/angular';

import { SigninComponent } from './signin/signin.component';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UIRouterModule
  ],
  declarations: [SigninComponent]
})
export class PublicModule { }
