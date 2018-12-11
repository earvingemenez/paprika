import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UIRouterModule } from '@uirouter/angular';

import { HelpersModule } from '../../commons/directives/helpers/helpers.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProfileComponent } from './profile/profile.component';


@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UIRouterModule,
    HelpersModule
  ],
  declarations: [DashboardComponent, ProfileComponent]
})
export class UsersModule { }
