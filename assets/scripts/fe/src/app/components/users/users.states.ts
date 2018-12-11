import { ContentOnly, NavContent } from '../../commons/utils/layout.utils';
import { LoginRequired } from '../../commons/utils/security.utils';

import { DashboardComponent } from './dashboard/dashboard.component';
import { ProfileComponent } from './profile/profile.component';


export const USERS_STATES : Object[] = [
  {
    name    : 'dashboard',
    url     : '/dashboard/',
    views   : NavContent(DashboardComponent),
    onEnter : LoginRequired
  },
  {
    name    : 'profile',
    url     : '/u/:handle/',
    views   : NavContent(ProfileComponent),
    onEnter : LoginRequired
  }
]