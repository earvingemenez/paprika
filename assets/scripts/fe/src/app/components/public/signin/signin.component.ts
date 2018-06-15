import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

import { StateService } from '@uirouter/angular';

import { LoginForm } from '../../../commons/structs/login.structs';
import { AuthService } from '../../../commons/services/auth/auth.service';


@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  LoginForm;

  constructor(
    private fb    : FormBuilder,
    private auth  : AuthService,
    private state : StateService
  ) { }

  ngOnInit() {
    this.LoginForm = new LoginForm(this.fb);
  }

  login () {
    let l = this.auth.login(this.LoginForm.form.value);

    l.catch(err => {
      this.LoginForm.invalidcreds = true;
    })

    l.then(resp => {
      this.state.go('dashboard');
    });
  }

}
