import { TestBed, inject } from '@angular/core/testing';

import { XsrfService } from './xsrf.service';

describe('XsrfService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [XsrfService]
    });
  });

  it('should be created', inject([XsrfService], (service: XsrfService) => {
    expect(service).toBeTruthy();
  }));
});
