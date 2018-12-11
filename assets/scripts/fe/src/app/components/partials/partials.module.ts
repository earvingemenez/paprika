import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { UIRouterModule } from '@uirouter/angular';

import { HttpdModule } from '../../commons/directives/httpd/httpd.module';

import { NavigationComponent } from './navigation/navigation.component';

@NgModule({
  imports: [
    CommonModule,
    NgbModule,
    HttpdModule,
    ReactiveFormsModule,
    UIRouterModule
  ],
  declarations: [NavigationComponent]
})
export class PartialsModule { }
