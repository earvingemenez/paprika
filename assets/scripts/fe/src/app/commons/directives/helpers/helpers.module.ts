import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RatingsDirective } from './ratings.directive';

@NgModule({
  imports: [
    CommonModule
  ],
  exports: [RatingsDirective],
  declarations: [RatingsDirective]
})
export class HelpersModule { }
