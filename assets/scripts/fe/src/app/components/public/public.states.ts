import { ContentOnly } from '../../commons/utils/layout.utils';
import { Disconnect } from '../../commons/utils/security.utils';

import { SigninComponent } from './signin/signin.component';


export const PUBLIC_STATES : Object[] = [
  {
    name  : 'signin',
    url   : '/login/',
    views : ContentOnly(SigninComponent)
  },
  {
    name    : 'signout',
    url     : '/logout/',
    onEnter : Disconnect
  }
]