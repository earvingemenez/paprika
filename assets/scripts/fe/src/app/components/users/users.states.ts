import { LoginRequired } from '../../commons/utils/security.utils';
import { ContentOnly } from '../../commons/utils/layout.utils';

import { DashboardComponent } from './dashboard/dashboard.component';


export const USERS_STATES : Object[] = [
    {
      name    : 'dashboard',
      url     : '/dashboard/',
      views   : ContentOnly(DashboardComponent),
      onEnter : LoginRequired
    },
]