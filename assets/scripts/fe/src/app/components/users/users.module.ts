import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { UIRouterModule } from '@uirouter/angular';
import { SwiperModule, SWIPER_CONFIG } from 'ngx-swiper-wrapper';

import { DEFAULT_SWIPER_CONFIG } from '../../commons/constants/conf.constants';

import { HelpersModule } from '../../commons/directives/helpers/helpers.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProfileComponent } from './profile/profile.component';


@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UIRouterModule,
    HelpersModule,
    SwiperModule
  ],
  declarations: [DashboardComponent, ProfileComponent],
  providers: [
    { provide: SWIPER_CONFIG, useValue: DEFAULT_SWIPER_CONFIG }
  ]
})
export class UsersModule { }
