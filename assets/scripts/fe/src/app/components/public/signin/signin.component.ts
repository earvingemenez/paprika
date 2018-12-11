import { Component, OnInit } from '@angular/core';
import { StateService } from '@uirouter/angular';

import { SignInForm } from '../../../commons/forms/signin.forms';
import { SignIn } from '../../../commons/models/signin.models';

import { AuthService } from '../../../commons/services/auth/auth.service';


@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  private form : SignInForm;

  constructor(
    private auth  : AuthService,
    private state : StateService
  ) { }

  ngOnInit() {
    // initialize the form.
    this.form = new SignInForm(new SignIn);
  }

  onSubmit ({ value, valid }: { value: SignIn, valid: boolean }) {
    // submit if all the credentials are valid.
    if (valid) {
      this.auth.signin(value)
        .then(resp => {
          this.state.go('dashboard');
        })
        .catch(err => {
          this.form.err = err;
        })
      ;
    }
  }

}