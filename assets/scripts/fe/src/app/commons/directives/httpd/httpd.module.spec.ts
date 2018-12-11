import { HttpdModule } from './httpd.module';

describe('HttpdModule', () => {
  let httpdModule: HttpdModule;

  beforeEach(() => {
    httpdModule = new HttpdModule();
  });

  it('should create an instance', () => {
    expect(httpdModule).toBeTruthy();
  });
});
