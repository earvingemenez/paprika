import { FormBuilder, FormGroup, Validators } from '@angular/forms';


export class LoginForm {
  form;
  invalidcreds = false;

  constructor (
    private fb : FormBuilder
  ) {
    this.form = this.fb.group(this.getFields());
  }

  getFields () {
    return {
      email : [null, Validators.required],
      password : [null, [Validators.required]]
    }
  }

  valid(f) {
    return !(!this.form.get(f).valid && this.form.get(f).touched);
  }
}