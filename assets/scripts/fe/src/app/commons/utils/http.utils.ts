/* Re-format the URL parameters for
 * readbility
 */
export function urlsafe (url, ...params) {
    return url.concat(params.join("/"), '/');
}