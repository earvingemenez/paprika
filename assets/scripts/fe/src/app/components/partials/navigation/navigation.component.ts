import { Component, OnInit } from '@angular/core';
import { NgbDropdownConfig } from '@ng-bootstrap/ng-bootstrap';

import { AuthService } from '../../../commons/services/auth/auth.service';


@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css'],
  providers: [NgbDropdownConfig]
})
export class NavigationComponent implements OnInit {

  constructor(
    private auth : AuthService,
    config: NgbDropdownConfig
  ) {
    // dropdown direction
    config.placement = 'bottom-right';
  }

  ngOnInit() {
    this.auth.getuser();
  }

}
