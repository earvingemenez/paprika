import { Directive, ElementRef, TemplateRef, ViewContainerRef, Renderer2, Input } from '@angular/core';

@Directive({
  selector: '[ratings]'
})
export class RatingsDirective {
  private stars : number[] = [1,2,3,4,5];

  constructor(
    private vcr : ViewContainerRef,
    private template : TemplateRef<any>,
    private el : ElementRef,
    private renderer : Renderer2
  ) { }

  @Input()
  set ratings(rate) {
    this.stars.forEach(i => {
      this.vcr.createEmbeddedView(this.template);
    });
  }
}
