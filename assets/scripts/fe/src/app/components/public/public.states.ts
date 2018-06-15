import { ContentOnly } from '../../commons/utils/layout.utils';

import { SigninComponent } from './signin/signin.component';


export const PUBLIC_STATES : Object[] = [
    { name: 'login', url: '/login/', views: ContentOnly(SigninComponent) },
]