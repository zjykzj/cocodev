<div align="right">
  Language:
    🇺🇸
  <!-- <a title="Chinese" href="./README.zh-CN.md">🇨🇳</a> -->
</div>

<div align="center"><a title="" href="https://github.com/zjykzj/cocodev"><img align="center" src="./imgs/cocodev.png" alt=""></a></div>

<p align="center">
  «cocodev» saved some documents, code, and tools for COCO
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square" alt=""></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg" alt=""></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" alt=""></a>
</p>

* Get COCO dataset 
  * By using script [get_coco.sh](./get_coco.sh), the COCO dataset train2017/val2017 can be obtained. 
  * After completing the run, you can find the corresponding data in `../datasets/coco`
* Convert COCO dataset to YOLOv5 format
  * [py/coco2yolov5.py](py/coco2yolov5.py)
* Convert COCOLike data to YOLOv5 format
  * [py/cocolike2yolov5.py](py/cocolike2yolov5.py)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Background](#background)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

[COCO](https://cocodataset.org/#home/) is the most influential object detection dataset, and currently the most advanced object detection algorithms usually use it as the benchmark dataset. This warehouse stores the code and tools I commonly use when processing COCO datasets,

## Maintainers

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## Contributing

Anyone's participation is welcome! Open an [issue](https://github.com/zjykzj/cocodev/issues) or submit PRs.

Small note:

* Git submission specifications should be complied
  with [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)
* If versioned, please conform to the [Semantic Versioning 2.0.0](https://semver.org) specification
* If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme)
  specification.

## License

[Apache License 2.0](LICENSE) © 2023 zjykzj