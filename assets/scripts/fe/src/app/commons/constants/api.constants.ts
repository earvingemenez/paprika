import { urlsafe } from '../utils/http.utils';

/* USERS ENDPOINTS
 */
export const USERS = '/api/users/';


/* AUTH ENDPOINTS
 */
export const AUTH_USER = urlsafe(USERS, 'auth');
export const AUTH_SIGNIN = urlsafe(AUTH_USER, 'login');

/* BOOKS ENDPOINTS
 */
export const BOOKS = '/api/books/';
export const READS = urlsafe(BOOKS, 'reads');
export const RELEASES = urlsafe(BOOKS, 'releases');