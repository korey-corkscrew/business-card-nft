// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./openzeppelin/contracts/security/Pausable.sol";
import "./openzeppelin/contracts/access/Ownable.sol";
import "./openzeppelin/contracts/utils/math/SafeMath.sol";


contract BusinessCardNFTV2 is ERC721, Pausable, Ownable {
    using SafeMath for uint256;

    uint256 public totalSupply;
    string public businessCardURI;

    constructor(
        string memory name_, 
        string memory symbol_,
        string memory URI_
    ) ERC721(name_, symbol_) {
        businessCardURI = URI_;
    }

    function mint() public whenNotPaused {
        _safeMint(msg.sender, totalSupply++);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }
}